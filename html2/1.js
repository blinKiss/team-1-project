// JavaScript 코드
const button = document.querySelector('.toggle-menu-button');
const menuList = document.querySelector('.toggle-menu-list');

button.addEventListener('click', () => {
  menuList.classList.toggle('show');
});
