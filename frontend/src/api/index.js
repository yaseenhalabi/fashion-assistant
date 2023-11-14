// place files you want to import through the `$lib` alias in this folder.
import axios from "axios";

export const getProducts = async(num_of_items) => {
  var data
  
  await axios.get("http://localhost:8000/api/getProducts/", {
    params: {
      num_of_items: num_of_items
    }
  })
    .then(response => {
      data = response.data
      data = data.map(item => ({...item, rating: "0"}))
    })
  return data
}

export const getProductMatches = async(preferences, rated_products) => {
    
  var data

  try {
    await axios.post("http://localhost:8000/api/getProductMatches/", rated_products, 
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


