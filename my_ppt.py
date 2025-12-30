import streamlit as st
import time
import streamlit.components.v1 as components

# 1. 设置页面配置
st.set_page_config(page_title="我的超级演示", layout="wide", page_icon="🎤")

# === 核心逻辑：侧边栏大纲 ===
st.sidebar.title("📑 演示大纲")
slides = ["封面：为什么选 Streamlit?", "第二页：交互式图表", "第三页：SD 作品展示", "结尾：大家来讨论"]
current_slide = st.sidebar.radio("跳转到：", slides)

# === 第一页：封面 ===
if current_slide == "封面：为什么选 Streamlit?":
    st.title("🎤 告别死板 PPT，拥抱 Streamlit")
    st.markdown("### —— 这是一个由 Python 代码生成的演示文稿")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=400)
    if st.button("点我开始演示"):
        st.balloons()

# === 第二页：交互图表 ===
elif current_slide == "第二页：交互式图表":
    st.header("📊 实时交互演示")
    number = st.slider("调整数值查看图表变化", 1, 100, 50)
    st.bar_chart({"数据A": number, "数据B": 100 - number})

# === 第三页：作品展示 ===
elif current_slide == "第三页：SD 作品展示":
    st.header("🎨 我的 AI 艺术画廊")
    col1, col2 = st.columns(2)
    with col1:
        st.image("20251230_081251_737.png", caption="赛博朋克风")
    with col2:
        st.image("20251230_081230_532.png", caption="二次元风格")

# === 第四页：Giscus 互动留言板 ===
elif current_slide == "结尾：大家来讨论":
    st.title("💬 互动留言板")
    st.write("欢迎在下方留言！评论将同步至 GitHub Discussions。")

    # 嵌入 Giscus 评论组件 (已针对你的仓库配置)
    components.html(
        """
        <script src="https://giscus.app/client.js"
            data-repo="LIUXIALAIHAHAHA/my-online-ppt"
            data-repo-id="R_kgDONn5Eag"
            data-category="Announcements"
            data-category-id="DIC_kwDONn5Eas4Cl4S_"
            data-mapping="pathname"
            data-strict="0"
            data-reactions-enabled="1"
            data-emit-metadata="0"
            data-input-position="top"
            data-theme="preferred_color_scheme"
            data-lang="zh-CN"
            crossorigin="anonymous"
            async>
        </script>
        """,
        height=600,
        scrolling=True,
    )
    st.info("提示：首次留言需要登录 GitHub 账号授权。")
