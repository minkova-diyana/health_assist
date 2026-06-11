const hInsuranceMenuElements = document.querySelectorAll('.insurance')


function showInfo(event){
    parent = event.target.closest('.insurance');

    const clickedElement = event.target;
    const insuranceInfo = document.getElementById(clickedElement.getAttribute('data-info'))

    if (insuranceInfo.style.display === 'none'){
        insuranceInfo.style.display = 'block';
    }
    else {
        insuranceInfo.style.display = 'none';
    }

}

hInsuranceMenuElements.forEach((element) => {
    element.addEventListener('click', showInfo)
    });