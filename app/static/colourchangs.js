window.onload = function () {
  alert("Welcome to the page!");
};
function appendCardTitlesToList() {
  const Comments = document.querySelectorAll(".comment");
  // Create an unordered list element

  //   for (const comment of Comments) {
  //     alert(comment.textContent);
  //     //comment.style.colour = "red";
  //   }
  Comments.forEach((Comments) => {
    Comments.style.color = "red";
    const Links = Comments.querySelectorAll("a");
    Links.forEach((Links) => {
      alert(Links.textContent);
      Links.classList.toggle("link-blue");
    });
  });
}
// Call the function to execute the logic
appendCardTitlesToList();
