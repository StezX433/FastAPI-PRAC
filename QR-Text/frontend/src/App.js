
import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [text, setText] = useState("");
  const [qrImage, setQrImage] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const generateQr = async () => {
    if (!text.trim()) {
      setError("Please enter text to generate QR code");
      return;
    }

    setLoading(true);
    setError("");
    setQrImage("");

    try {
      const response = await fetch("http://127.0.0.1:8000/generate_qr", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();

      if (response.ok) {
        setQrImage(`data:image/png;base64,${data.qr_code}`);
      } else {
        setError(data.error || "Failed to generate QR code");
      }
    } catch {
      setError("Server not responding");
    }

    setLoading(false);
  };

  return (
    <div className="container py-5 text-center">
      <h2 className="mb-4">Text to QR Code Converter</h2>

      <div className="mb-3">
        <textarea
          className="form-control"
          placeholder="Enter text here..."
          rows="3"
          value={text}
          onChange={(e) => setText(e.target.value)}
        ></textarea>
      </div>

      <button
        className="btn btn-primary"
        onClick={generateQr}
        disabled={loading}
      >
        {loading ? "Generating..." : "Generate QR Code"}
      </button>

      {error && (
        <div className="alert alert-danger mt-3">
          {error}
        </div>
      )}

      {qrImage && (
        <div className="mt-4">
          <h5>Your QR Code:</h5>
          <img
            src={qrImage}
            alt="QR Code"
            className="img-fluid border p-2 mt-2"
            style={{ maxWidth: "250px" }}
          />
        </div>
      )}
    </div>
  );
}

export default App;
