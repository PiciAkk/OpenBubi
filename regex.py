import re

txt = "<div class='fw-light d-flex align-items-center justify-content-center col-10 offset-1 col-sm-4 offset-sm-0 col-lg-4 py-3 py-sm-0'>Érvényeség vége: 23.08.2022</div>"
x = re.findall("Érvényeség vége: .*</div>$", txt)

x = x[0]
x = x.replace("Érvényeség vége: ",  "").replace("</div>", "")
print(x)
