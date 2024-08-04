const API_BASE_URL = "http://localhost:5000/api";

// async function handleResponse(response) {
//   if (!response.ok) {
//     const error = await response.text();
//     throw new Error(error);
//   }
//   return response.json();
// }

// Function to login user
export async function loginUser(email) {
  const response = await fetch(`${API_BASE_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email }),
  });
  if (!response.ok) throw new Error("Login failed");
  return response.json();
}

// Function to register user
export async function registerUser(email, preferences) {
  const response = await fetch(`${API_BASE_URL}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, preferences }),
  });
  if (!response.ok) throw new Error("Registration failed");
  return response.json();
}

// Function to save user preferences
export async function savePreferences(email, preferences, token) {
  const response = await fetch(`${API_BASE_URL}/preferences`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ email, preferences }),
  });
  if (!response.ok) throw new Error("Failed to save preferences");
  return response.json();
}

// Function to fetch news summaries
export async function fetchNewsSummaries(email) {
  const response = await fetch(`${API_BASE_URL}/news`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email }),
  });
  if (!response.ok) throw new Error("Failed to fetch news summaries");
  return response.json();
}
