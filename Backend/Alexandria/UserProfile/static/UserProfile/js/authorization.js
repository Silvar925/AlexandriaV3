const btnSignIn = document.getElementById('btnSignIn')

const btnCreate = document.getElementById("btnCreate");

btnCreate.addEventListener('click', function() {
    const contentContainers = document.querySelectorAll('.content-container');
    contentContainers.forEach(el => el.classList.add('hidden'));
    
    const temp = document.querySelector('.regisration');
    temp.classList.remove('hidden');
})

const btnCancel = document.getElementById("btnCancel");

btnCancel.addEventListener('click', function() {
    const contentContainers = document.querySelectorAll('.content-container');
    contentContainers.forEach(el => el.classList.add('hidden'));
    
    const temp = document.querySelector('.authorization');
    temp.classList.remove('hidden');
});

const btnCreateID = document.getElementById("btnCreateID");

btnCreateID.addEventListener('click', function() {
    const lineSurname = getTextFromInput("lineSurname");
    const lineName = getTextFromInput("lineName");
    const lineEmail = getTextFromInput("lineEmail");
    const lineLogin = getTextFromInput("lineLoginReg");
    const linePassword = getTextFromInput("linePasswordReg");
});
