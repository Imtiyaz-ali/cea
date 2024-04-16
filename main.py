import re

lis = ["Other Allowance","Gross Salary","CPF Subscription","CPF Arrer","CPF Loan Amount","CPF Loan Instalment","Income Tax","LIC","Excess Pay Recovery","Other Recovery","Installment Of Other Recovery",'Society Loan Recovery','Installment Of Society Loan Recovery',"GIS","SLI","Excess DA Recovery","Installment of Excess DA Recovery","GPAIS","Professional Tax","Total Deduction","Net Pay","Arear CPF Contribution","CPF Contribution","Gratuity","Increment Date"]


def generate_class_names(items):
    class_names = []
    for item in items:
        # Remove non-alphanumeric characters and replace spaces with underscores
        class_name = re.sub(r'\W+', '_', item.strip())
        # Add a prefix to make it a valid class name
        class_names.append(class_name)
    return class_names


f= open("try.html","a")

classes = []
for i in lis:
    className = generate_class_names(i)
    # id = className + "_input"
    print("class Name: ",className)
    # print("id Name: ",id)

    str = f"""<!-- HRA -->r
          <div class="hra">
            <label for="hra"></label>
            <input type="text" placeholder="HRA" name="hra" id="hra_input" disabled required>
          </div>"""
    f.write(f"{i} \n")

f.close()