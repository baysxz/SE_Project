fetch("http://localhost:5001/items")
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("list");

    data.forEach(item => {
      const div = document.createElement("div");
      div.className = "card";

      div.innerHTML = `
        <div class="title">${item.title}</div>
        <div>${item.description}</div>
      `;

      container.appendChild(div);
    });
  })
  .catch(err => console.log("Error:", err));
