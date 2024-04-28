import axios from "axios";

export const getProductMatches = async(preferences, selected_images) => {
  var data
  try {
    await axios.post("http://localhost:8000/api/getProducts", 
      selected_images, 
      {
        headers: {'Content-Type': 'application/json'},
        params: preferences
      }
    ).then(response => {data = response.data})
  } catch (error) {
    console.log(error)
  }
  return data
}


