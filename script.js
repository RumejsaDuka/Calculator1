function press(value) {
    document.getElementById("display").value += value;
}

function calculate() {
    let display = document.getElementById("display");
    try {
        display.value = eval(display.value);
    } catch {
        display.value = "Gabim!";
    }
}

function clearDisplay() {
    document.getElementById("display").value = "";
}
