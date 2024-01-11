const header = document.getElementById('header')
const nav = document.createElement('nav')

nav.innerHTML = `<h1>Александрия</h1>
<ul>
    <li><a href="#">Главная</a></li>
    <li><a href="#">Тренажер</a></li>
    <li><a href="#">Магазин</a></li>
    <li><a href="#">О нас</a></li>
</ul>

<div class="profile_container">
    <div class="profile_container_img">
        <img src="images/av4.png" alt="#">
    </div>

    <div class="profile_container_active">
        <p>Хатидже Сафина</p>
        <select name="" id="">
            <option value="">Профиль</option>
            <option value="">Выйти</option>
        </select>
    </div>
</div>`

header.appendChild(nav)