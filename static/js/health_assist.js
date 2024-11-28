const hInsuranceMenueElements = document.querySelectorAll('.insurance')

function showInfo(event){
    const allInfoElements = document.querySelectorAll('.sub-container');
    allInfoElements.forEach(infoElement => {
        infoElement.style.display = 'none';

    });

    const clickedElement = event.target;
    const insuranceInfo = document.getElementById(clickedElement.getAttribute('data-info'))
    insuranceInfo.style.display = 'flex';

}

hInsuranceMenueElements.forEach((element) => {
    element.addEventListener('click', showInfo)
    });