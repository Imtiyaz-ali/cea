function AddTotal(){
    var num1 = parseFloat(document.getElementById('pay_input').value);
    var num2 = parseFloat(document.getElementById('agp_input').value);
    var sum = num1 + num2;
    document.getElementById('total_input').value = sum;
}

document.getElementById("pay_input").addEventListener("input", AddTotal);
document.getElementById('agp_input').addEventListener('input', AddTotal);

