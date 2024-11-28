const hInsuranceMenuElements = document.querySelectorAll('.insurance')


function showInfo(event){
    parent = event.target.closest('.insurance');
    const allInfoElements = parent.querySelectorAll('.sub-container');
    allInfoElements.forEach(infoElement => {
        infoElement.style.display = 'none';

    });

    const clickedElement = event.target;
    const insuranceInfo = document.getElementById(clickedElement.getAttribute('data-info'))
    insuranceInfo.style.display = 'flex';

}

hInsuranceMenuElements.forEach((element) => {
    element.addEventListener('click', showInfo)
    });

