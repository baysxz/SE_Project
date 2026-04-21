fetch("http://localhost:5001/users")
  .then((res) => res.json())
  .then((data) => {
    console.log(data);

    const container = document.getElementById("list");

    data.forEach((s) => {
      const div = document.createElement("div");
      div.innerHTML = `
        <h3>${s.name}</h3>
        <p>${s.email}</p>
      `;
      container.appendChild(div);
    });
  });
