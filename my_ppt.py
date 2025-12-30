import streamlit as st
import time
# 必须放在顶部的导入语句
from streamlit_disqus import st_disqus

# 1. 设置页面配置 (网页标题，宽屏模式)
st.set_page_config(page_title="我的超级演示", layout="wide", page_icon="🎤")

# === 核心逻辑：用侧边栏模拟 PPT 的“目录” ===
st.sidebar.title("📑 演示大纲")
slides = ["封面：为什么选 Streamlit?", "第二页：交互式图表", "第三页：SD 作品展示", "结尾：大家来讨论"]
current_slide = st.sidebar.radio("跳转到：", slides)

# === 第一页：封面 ===
if current_slide == "封面：为什么选 Streamlit?":
    st.title("🎤 告别死板 PPT，拥抱 Streamlit")
    st.markdown("### —— 这是一个由 Python 代码生成的演示文稿")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=400)
    st.info("💡 这是一个活的网页，不仅仅是图片！")
    if st.button("点我开始演示"):
        st.balloons()

# === 第二页：展示交互能力 ===
elif current_slide == "第二页：交互式图表":
    st.header("📊 传统 PPT 做不到的事：实时交互")
    st.write("在传统 PPT 里，数据是死的。但在这里，**你说了算**：")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("参数控制")
        number = st.slider("请选择一个数字", 1, 100, 50)
        color = st.color_picker("给柱状图选个颜色", "#00f900")
    with col2:
        st.subheader("实时反馈")
        chart_data = {"数据A": number, "数据B": 100 - number}
        st.bar_chart(chart_data, color=color)
        st.caption(f"图表随着你的操作在实时变化！当前数值：{number}")

# === 第三页：展示你的 SD 专长 ===
elif current_slide == "第三页：SD 作品展示":
    st.header("🎨 我的 AI 艺术画廊")
    tab1, tab2 = st.tabs(["赛博朋克风", "二次元风格"])
    with tab1:
        st.write("这是用 Stable Diffusion 生成的未来城市...")
        # 确认你的图片文件名与 GitHub 仓库中完全一致（包括后缀）
        st.image("20251230_081251_737.png", caption="赛博朋克艺术作品")
    with tab2:
        st.write("这是二次元模型生成的角色...")
        st.image("20251230_081230_532.png", caption="二次元动漫风格")

# === 第四页：专业留言板 (不再有语法错误) ===
elif current_slide == "结尾：大家来讨论":
    st.title("💬 留言讨论区")
    st.write("欢迎在这里留下你的足迹！")
    # 使用唯一的 ID 来标识这个留言板
    st_disqus("my-cool-ppt-2025-v1")
    st.success("提示：留言内容将永久保存，大家刷新网页也能看到。")
