import glob
import re

html_files = glob.glob('d:/ZID/PLATA-THEME/**/*.html', recursive=True)

new_desktop_nav = """          <nav class="desktop-nav">
            <a href="/" class="nav-link">الرئيسية</a>
            <a href="/pages/category/index.html" class="nav-link">تسوق</a>
            <a href="/pages/routines/index.html" class="nav-link">الروتين</a>
            <a href="/pages/product/index.html" class="nav-link">المنتج</a>
            <a href="/pages/cart/index.html" class="nav-link">السلة</a>
            <a href="/pages/quiz/index.html" class="nav-link">اختبار البشرة</a>
          </nav>"""

new_mobile_nav = """      <nav class="mobile-menu-links">
        <a href="/" class="mobile-nav-link">الرئيسية</a>
        <a href="/pages/category/index.html" class="mobile-nav-link">تسوق</a>
        <a href="/pages/routines/index.html" class="mobile-nav-link">الروتين</a>
        <a href="/pages/product/index.html" class="mobile-nav-link">المنتج</a>
        <a href="/pages/cart/index.html" class="mobile-nav-link">السلة</a>
        <a href="/pages/quiz/index.html" class="mobile-nav-link">اختبار البشرة</a>
      </nav>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace desktop nav
    content = re.sub(r'<nav class="desktop-nav">.*?</nav>', new_desktop_nav, content, flags=re.DOTALL)
    
    # Replace mobile nav
    content = re.sub(r'<nav class="mobile-menu-links">.*?</nav>', new_mobile_nav, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated nav in all HTML files!")
