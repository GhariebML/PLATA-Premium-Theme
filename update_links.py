import os
import glob
import re

html_files = glob.glob('d:/ZID/PLATA-THEME/**/*.html', recursive=True)

new_links = """        <div class="footer-column">
          <h4 class="footer-heading">استكشفي</h4>
          <nav class="footer-links">
            <a href="/" class="footer-link">الرئيسية</a>
            <a href="/pages/category/index.html" class="footer-link">تسوقي المنتجات</a>
            <a href="/pages/routines/index.html" class="footer-link">روتين العناية</a>
          </nav>
        </div>
        <div class="footer-column">
          <h4 class="footer-heading">تسوق سريع</h4>
          <nav class="footer-links">
            <a href="/pages/product/index.html" class="footer-link">تفاصيل المنتج</a>
            <a href="/pages/cart/index.html" class="footer-link">سلة المشتريات</a>
            <a href="/pages/quiz/index.html" class="footer-link">اختبار البشرة</a>
          </nav>
        </div>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace footer links
    pattern = re.compile(r'<div class="footer-column">\s*<h4 class="footer-heading">استكشفي</h4>.*?</div>\s*<div class="footer-column">\s*<h4 class="footer-heading">المساعدة</h4>.*?</div>', re.DOTALL)
    content = pattern.sub(new_links, content)
    
    # Replace header and button links globally to ensure robust navigation
    content = content.replace('href="/shop"', 'href="/pages/category/index.html"')
    content = content.replace('href="/categories"', 'href="/pages/category/index.html"')
    content = content.replace('href="/routines"', 'href="/pages/routines/index.html"')
    content = content.replace('href="/cart"', 'href="/pages/cart/index.html"')
    content = content.replace('href="/quiz"', 'href="/pages/quiz/index.html"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated links successfully!')
