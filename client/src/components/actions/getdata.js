export function getProfiledata(token_data) {
  return fetch("/user/profile", {
    method: "GET",
    headers: { Authorization: token_data },
  }).then((response) => {
      console.log(response)
    return response.json()
  });
}

// export const getSignInData = (data) => {
//   console.log(data)
//     fetch("/signin", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify(data),
//       }).then(response => {
//           console.log(response)
//         return response.json()
//       })
// }
