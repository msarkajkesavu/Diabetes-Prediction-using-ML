const menu = document.querySelector('#mobile-menu')
const menuLinks = document.querySelector('.head_menu')

menu.addEventListener('click', function() {
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
})

function calculateAge() {
    var dob = document.getElementById("date-of-birth").value;
    var today = new Date();
    var birthDate = new Date(dob);
    var age = today.getFullYear() - birthDate.getFullYear();
    // Adjust for different month/day combinations
    var m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    document.getElementById("age").value = age;
}

function calculateBMI() {
    const weight = parseFloat(document.getElementById("weightInput").value);
    const heightInCm = parseFloat(document.getElementById("heightInput").value);

    if ((!isNaN(weight) && weight > 0) && (!isNaN(heightInCm) && heightInCm > 0)) {
        // Convert height from cm to meters
        const heightInM = heightInCm / 100;

        const bmi = weight / (heightInM * heightInM);
        document.getElementById("bmiInput").value = bmi.toFixed(2);
    } else {
        document.getElementById("bmiInput").value = ""; // Clear BMI if invalid input
    }
}

// Attach input event listeners to recalculate BMI on input change
document.getElementById("weightInput").addEventListener("input", calculateBMI);
document.getElementById("heightInput").addEventListener("input", calculateBMI);

// Optionally, you can trigger the calculation when the page loads
document.addEventListener("DOMContentLoaded", calculateBMI);


// Display the current value of the slider
document.getElementById("HbA1c_level").addEventListener("input", function() {
    document.getElementById("sliderValue").innerText = this.value;
});