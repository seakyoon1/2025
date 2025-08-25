import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# -------------------------------
# App Config
# -------------------------------
st.set_page_config(page_title="세포 분열 시뮬레이터 (유사분열)", page_icon="🧫", layout="wide")

st.title("🧫 세포 분열 시뮬레이터 : 유사분열(Mitosis)")
st.write(
    "슬라이더 또는 ▶️ 애니메이션으로 **간기 → 전기 → 중기 → 후기 → 말기 → 세포질 분열** 단계를 시각적으로 살펴보세요.\n"
    "각 단계에서 핵막, 염색체, 방추사(미세소관)의 변화를 단순화하여 도식으로 표현합니다."
)

# -------------------------------
# Stage Definitions
# -------------------------------
stages = [
    {"key": 0, "name": "간기 (Interphase)", "desc": "DNA가 복제되고(2배) 세포가 분열 준비를 함. 핵막이 유지되고 염색사가 퍼져 있어 개별 염색체가 잘 보이지 않음."},
    {"key": 1, "name": "전기 (Prophase)", "desc": "염색사가 응축되어 염색체가 보이기 시작. 중심체가 이동하며 방추사(미세소관)가 형성. 핵막이 점차 붕괴."},
    {"key": 2, "name": "중기 (Metaphase)", "desc": "염색체가 방추사의 당김으로 세포의 적도판(가운데)에 배열."},
    {"key": 3, "name": "후기 (Anaphase)", "desc": "자매염색분체가 분리되어 양극(세포 양쪽)으로 이동."},
    {"key": 4, "name": "말기 (Telophase)", "desc": "양극에 도달한 염색체가 풀리며 핵막 재형성. 방추사 분해."},
    {"key": 5, "name": "세포질 분열 (Cytokinesis)", "desc": "세포질이 분리되어 두 개의 딸세포 완성. 동물세포는 수축환으로 잘록해지고, 식물세포는 세포판 형성."},
]

# -------------------------------
# Sidebar Controls
# -------------------------------
st.sidebar.header("⚙️ 컨트롤")
cell_type = st.sidebar.selectbox("세포 유형(도식)", ["동물세포", "식물세포"], index=0)
num_chrom = st.sidebar.slider("염색체 쌍(도식적 수)", 2, 8, 4, help="시각화용 단순 수치")
show_spindle = st.sidebar.checkbox("방추사 표시", value=True)
show_centrosome = st.sidebar.checkbox("중심체/극 표시", value=True)

speed = st.sidebar.slider("애니메이션 속도(초)", 0.1, 1.5, 0.5, 0.1)
autoplay = st.sidebar.checkbox("▶️ 자동 재생", value=False)

if "frame" not in st.session_state:
    st.session_state.frame = 0

# -------------------------------
# Drawing Utilities
# -------------------------------

def draw_cell(ax, stage_idx, cell_type, num_chrom, show_spindle, show_centrosome):
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')

    # Canvas bounds
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)

    # Cell boundary
    circle = plt.Circle((0, 0), 1.0, fill=False, linewidth=2)
    ax.add_artist(circle)

    # Cleavage furrow (animal) or cell plate (plant) at cytokinesis
    if stage_idx == 5:
        if cell_type == "동물세포":
            # indentation
            for y in np.linspace(-0.7, 0.7, 7):
                ax.plot([ -0.15*np.cos(np.pi*y), 0.15*np.cos(np.pi*y)], [y, y], linewidth=2, alpha=0.7)
        else:  # 식물
            ax.plot([0,0], [-1,1], linewidth=4, alpha=0.7)

    # Nucleus (present in interphase and telophase)
    if stage_idx in [0,4]:
        nucleus = plt.Circle((0, 0), 0.55, fill=False, linewidth=1.8, linestyle='--')
        ax.add_artist(nucleus)

    # Poles / Centrosomes
    if show_centrosome and stage_idx >= 1:
        pole_x = 0.85
        ax.scatter([-pole_x, pole_x], [0,0], s=80)

    # Spindle fibers (simplified)
    if show_spindle and stage_idx >= 1 and stage_idx <= 4:
        for ang in np.linspace(-0.9, 0.9, 9):
            ax.plot([-0.85, 0.0], [0, ang], linewidth=1, alpha=0.6)
            ax.plot([ 0.85, 0.0], [0, ang], linewidth=1, alpha=0.6)

    # Chromosomes (paired rods before anaphase separation)
    rng = np.random.default_rng(42)  # deterministic placement

    if stage_idx == 0:
        # Interphase: diffuse chromatin (draw dots inside nucleus)
        pts = rng.normal(size=(200,2), scale=0.22)
        pts = pts[np.linalg.norm(pts,axis=1) < 0.5]
        ax.scatter(pts[:,0], pts[:,1], s=5, alpha=0.4)
    elif stage_idx == 1:
        # Prophase: condensed chromosomes randomly placed
        for i in range(num_chrom):
            x = rng.uniform(-0.3,0.3); y = rng.uniform(-0.3,0.3)
            ax.plot([x-0.08, x+0.08],[y-0.15,y+0.15], linewidth=3)
            ax.plot([x+0.08, x-0.08],[y-0.15,y+0.15], linewidth=3)
    elif stage_idx == 2:
        # Metaphase: aligned at equator (x ~ 0)
        ys = np.linspace(-0.6,0.6,num_chrom)
        for y in ys:
            ax.plot([-0.08, 0.08],[y-0.15,y+0.15], linewidth=3)
            ax.plot([ 0.08,-0.08],[y-0.15,y+0.15], linewidth=3)
    elif stage_idx == 3:
        # Anaphase: sister chromatids separate to poles
        ys = np.linspace(-0.6,0.6,num_chrom)
        for y in ys:
            # left set
            ax.plot([-0.6,-0.25],[y-0.15,y+0.15], linewidth=3)
            ax.plot([-0.25,-0.6],[y-0.15,y+0.15], linewidth=3)
            # right set
            ax.plot([0.25,0.6],[y-0.15,y+0.15], linewidth=3)
            ax.plot([0.6,0.25],[y-0.15,y+0.15], linewidth=3)
    elif stage_idx == 4:
        # Telophase: chromosomes at poles, nuclei reform
        left_nuc = plt.Circle((-0.45, 0), 0.4, fill=False, linewidth=1.8, linestyle='--')
        right_nuc = plt.Circle((0.45, 0), 0.4, fill=False, linewidth=1.8, linestyle='--')
        ax.add_artist(left_nuc); ax.add_artist(right_nuc)
        ys = np.linspace(-0.35,0.35,num_chrom)
        for y in ys:
            ax.plot([-0.55,-0.35],[y-0.1,y+0.1], linewidth=2)
            ax.plot([-0.35,-0.55],[y-0.1,y+0.1], linewidth=2)
            ax.plot([ 0.35, 0.55],[y-0.1,y+0.1], linewidth=2)
            ax.plot([ 0.55, 0.35],[y-0.1,y+0.1], linewidth=2)
    elif stage_idx == 5:
        # Cytokinesis: two daughter cells suggested by membrane pinch/plate
        # Reuse telophase chromosome placement for simplicity
        ys = np.linspace(-0.35,0.35,num_chrom)
        for y in ys:
            ax.plot([-0.55,-0.35],[y-0.1,y+0.1], linewidth=2)
            ax.plot([-0.35,-0.55],[y-0.1,y+0.1], linewidth=2)
            ax.plot([ 0.35, 0.55],[y-0.1,y+0.1], linewidth=2)
            ax.plot([ 0.55, 0.35],[y-0.1,y+0.1], linewidth=2)

    ax.set_title(stages[stage_idx]["name"], pad=10)


# -------------------------------
# Main Layout
# -------------------------------
left, right = st.columns([2, 1])

with left:
    stage_idx = st.slider("단계", 0, len(stages)-1, st.session_state.frame,
                          format="%d", step=1, label_visibility="collapsed")

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111)
    draw_cell(ax, stage_idx, cell_type, num_chrom, show_spindle, show_centrosome)
    st.pyplot(fig, use_container_width=True)

with right:
    st.subheader(stages[stage_idx]["name"]) 
    st.write(stages[stage_idx]["desc"]) 

    st.markdown("---")
    st.markdown("**학습 포인트**")
    bullets = {
        0: ["DNA 복제 완료(2배)", "핵막 유지", "염색사는 퍼져 있음"],
        1: ["염색체 응축 시작", "핵막 붕괴", "방추사 형성"],
        2: ["적도판 배열", "각 염색체의 동원체가 방추사에 연결"],
        3: ["자매염색분체 분리", "양극으로 이동"],
        4: ["핵막 재형성", "염색체 이완"],
        5: ["세포질 분열로 2개의 딸세포", "동물: 수축환 / 식물: 세포판"],
    }
    st.write("\n".join([f"• {b}" for b in bullets[stage_idx]]))

    st.markdown("---")
    st.caption("도식은 이해를 돕기 위한 단순화 모델로 실제 세포 구조와 비율과 다를 수 있어요.")

# -------------------------------
# Autoplay Logic
# -------------------------------
if autoplay:
    next_frame = (stage_idx + 1) % len(stages)
    st.session_state.frame = next_frame
    time.sleep(float(speed))
    st.rerun()

