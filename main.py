import re

lis = ["Other Allowance","Gross Salary","CPF Subscription","CPF Arrer","CPF Loan Amount","CPF Loan Instalment","Income Tax","LIC","Excess Pay Recovery","Other Recovery","Installment Of Other Recovery",'Society Loan Recovery','Installment Of Society Loan Recovery',"GIS","SLI","Excess DA Recovery","Installment of Excess DA Recovery","GPAIS","Professional Tax","Total Deduction","Net Pay","Arear CPF Contribution","CPF Contribution","Gratuity","Increment Date"]


def generate_class_names(items):
    class_name = re.sub(r'\W+', '_', items.strip())

    return class_name.lower()


f= open("try.html","a")

classes = []
for i in lis:
    className = generate_class_names(i)
    id = className + "_input"

    str = f"""<!-- {i} -->
          <div class="{className}">
            <label for="{className}"></label>
            <input type="text" placeholder="{i}" name="{className}" id="{id}" required>
          </div>"""
    f.write(f"{str} \n \n")

f.close()