const classArray = [
  "link-red",
  "link-orange",
  "link-yellow",
  "link-yellow",
  "link-green",
  "link-blue",
];

window.onload = function () {
  alert("Welcome to the page!");
};
function appendCardTitlesToList() {
  const Comments = document.querySelectorAll(".comment");

  Comments.forEach((Comments) => {
    const Links = Comments.querySelectorAll("a");
    Links.forEach((Links) => {
      alert(Links.textContent);
      const randomIndex = Math.floor(Math.random() * classArray.length);
      const colourClass = classArray[randomIndex];

      Links.classList.toggle(colourClass);
    });
  });
}

appendCardTitlesToList();
