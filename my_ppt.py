import streamlit as st
import streamlit.components.v1 as components

# 1. 设置页面配置 (网页标题，宽屏模式)
st.set_page_config(page_title="我的超级演示", layout="wide", page_icon="🎤")

# === 核心逻辑：侧边栏目录 ===
st.sidebar.title("📑 演示大纲")
slides = ["封面：为什么选 Streamlit?", "第二页：交互式图表", "第三页：SD 作品展示", "结尾：匿名留言墙"]
current_slide = st.sidebar.radio("跳转到：", slides)

# === 第一页：封面 ===
if current_slide == "封面：为什么选 Streamlit?":
    st.title("🎤 告别死板 PPT，拥抱 Streamlit")
    st.markdown("### —— 这是一个由 Python 代码生成的演示文稿")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=400)
    st.info("💡 这是一个活的网页，不仅仅是图片！")
    if st.button("点我开始演示"):
        st.balloons()

# === 第二页：交互图表 ===
elif current_slide == "第二页：交互式图表":
    st.header("📊 实时交互演示")
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

# === 第三页：作品展示 ===
elif current_slide == "第三页：SD 作品展示":
    st.header("🎨 我的 AI 艺术画廊")
    tab1, tab2 = st.tabs(["赛博朋克风", "二次元风格"])
    
    with tab1:
        st.write("这是用 Stable Diffusion 生成的未来城市...")
        # 请确保文件名和你 GitHub 仓库里的一致
        st.image("20251230_081251_737.png", caption="赛博朋克艺术作品")
    
    with tab2:
        st.write("这是二次元模型生成的角色...")
        st.image("20251230_081230_532.png", caption="二次元动漫风格")

# === 第四页：Padlet 留言墙 (你的专属版) ===
elif current_slide == "结尾：匿名留言墙":
    st.title("💬 互动留言区")
    st.write("无需登录，双击墙面即可贴上你的便利贴！(支持手机和电脑)")

    # 这里是你刚才提供的专属 Padlet 嵌入代码
    padlet_html = """
    <div class="padlet-embed" style="border:1px solid rgba(0,0,0,0.1);border-radius:2px;box-sizing:border-box;overflow:hidden;position:relative;width:100%;background:#F4F4F4">
        <p style="padding:0;margin:0">
            <iframe src="https://padlet.com/embed/n9yzvial2taocuuf" frameborder="0" allow="camera;microphone;geolocation;display-capture;clipboard-write" style="width:100%;height:608px;display:block;padding:0;margin:0"></iframe>
        </p>
        <div style="display:flex;align-items:center;justify-content:end;margin:0;height:28px">
            <a href="https://padlet.com?ref=embed" style="display:block;flex-grow:0;margin:0;border:none;padding:0;text-decoration:none" target="_blank">
                <div style="display:flex;align-items:center;">
                    <img src="https://padlet.net/embeds/made_with_padlet_2022.png" width="114" height="28" style="padding:0;margin:0;background:0 0;border:none;box-shadow:none" alt="Made with Padlet">
                </div>
            </a>
        </div>
    </div>
    """
    
    # 渲染 HTML，高度设置得稍微大一点以免出现双滚动条
    components.html(padlet_html, height=650, scrolling=True)
