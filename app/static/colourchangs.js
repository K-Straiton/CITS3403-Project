const classArray = [
  "link-red",
  "link-orange",
  "link-yellow",
  "link-yellow",
  "link-green",
  "link-blue",
];

var userColours = [];

function appendCardTitlesToList() {
  const Comments = document.querySelectorAll(".comment");

  Comments.forEach((Comments) => {
    const Links = Comments.querySelectorAll("a");
    Links.forEach((Links) => {
      const randomIndex = Math.floor(Math.random() * classArray.length);
      const colourClass = classArray[randomIndex];
      Links.classList.toggle(colourClass);
    });
  });
}

appendCardTitlesToList();
