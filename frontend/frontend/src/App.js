import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState(null);

  // Call the backend API when the component mounts
  useEffect(() => {
    const backendUrl = "https://threed-virtual-tailor-1.onrender.com"; // Replace with your Render URL

    fetch(`${backendUrl}/api/models`)  // Replace with your actual endpoint
      .then(response => response.json())
      .then(data => setData(data))  // Store the data in state
      .catch(error => console.error("Error:", error));
  }, []);

  return (
    <div>
      <h1>3D Virtual Tailor</h1>
      <div>
        {data ? (
          <pre>{JSON.stringify(data, null, 2)}</pre>  // Display the data
        ) : (
          <p>Loading...</p>
        )}
      </div>
    </div>
  );
}

export default App;

