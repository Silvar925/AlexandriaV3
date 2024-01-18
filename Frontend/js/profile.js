const friendsBox = document.getElementById('friendsBox')
const messengerBox = document.getElementById('messengerBox')

const btnFriends = document.getElementById('btnFriends')
const btnMessenger = document.getElementById('btnMessenger')

let listContainers = [friendsBox, messengerBox]

btnFriends.addEventListener('click', function () {
    for (let i = 0; i < listContainers.length; i++) {
        if (listContainers[i].style.display != "none" &&  listContainers[i] != friendsBox) {
            listContainers[i].style.display = "none"

            friendsBox.style.display = "flex"
        }
    }
})

btnMessenger.addEventListener('click', function() {
    for (let i = 0; i < listContainers.length; i++) {
        if (listContainers[i].style.display != "none" &&  listContainers[i] != messengerBox) {
            listContainers[i].style.display = "none"

            messengerBox.style.display = "flex"
        }
    }
})