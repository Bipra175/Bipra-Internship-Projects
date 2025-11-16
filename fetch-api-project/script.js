let postList = document.getElementById("postList");
let loadMoreBtn = document.getElementById("loadMoreBtn");

let limit = 10;
let start = 0;

async function loadPosts() {
  const response = await fetch("https://jsonplaceholder.typicode.com/posts");
  const data = await response.json();
  const posts = data.slice(start, start + limit);

  posts.forEach(post => {
    const li = document.createElement("li");
    li.textContent = post.title;
    postList.appendChild(li);
  });

  start += limit;
  if (start >= data.length) {
    loadMoreBtn.style.display = "none";
  }
}

loadMoreBtn.addEventListener("click", loadPosts);
window.addEventListener("load", loadPosts);
