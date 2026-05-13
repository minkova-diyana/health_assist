const hInsuranceMenuElements = document.querySelectorAll('.insurance')
const showInfoPackageElements = document.querySelectorAll('.header')

function showInfo(event){
    parent = event.target.closest('.insurance');
    const allInfoElements = parent.querySelectorAll('.sub-container');
    allInfoElements.forEach(infoElement => {
        infoElement.style.display = 'none';

    });

    const clickedElement = event.target;
    const insuranceInfo = document.getElementById(clickedElement.getAttribute('data-info'))
    insuranceInfo.style.display = 'block';

}

function showMore(event) {
    const infoElement = event.currentTarget.nextElementSibling;

    if (infoElement && infoElement.classList.contains('insurance')) {
        infoElement.style.display = 'block';
    }
}


hInsuranceMenuElements.forEach((element) => {
    element.addEventListener('click', showInfo)
    });

showInfoPackageElements.forEach((element) => {
    element.addEventListener('click', showMore)
})

