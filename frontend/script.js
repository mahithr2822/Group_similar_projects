const backendUrl = "http://127.0.0.1:5000";

document.getElementById("uploadBtn").onclick = async () => {
  const files = document.getElementById("fileInput").files;
  if (files.length === 0) return alert("No files selected.");

  const formData = new FormData();
  for (let f of files) formData.append("files", f);

  const res = await fetch(`${backendUrl}/upload`, {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  alert(data.message);
};

document.getElementById("clusterBtn").onclick = async () => {
  const res = await fetch(`${backendUrl}/cluster`);
  const data = await res.json();
  const out = document.getElementById("output");
  out.innerHTML = "";

  for (const [cluster, docs] of Object.entries(data)) {
    const div = document.createElement("div");
    div.className = "cluster";
    div.innerHTML = `<h3>Cluster ${cluster}</h3><ul>${docs.map(d => `<li>${d}</li>`).join("")}</ul>`;
    out.appendChild(div);
  }
};
