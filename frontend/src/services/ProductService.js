import axios from "axios";

export const getProducts = async(num_of_items) => {
  var data
  
  await axios.get(`http://localhost:8000/api/getAvailableProducts/` + num_of_items.toString())
    .then(response => {
      data = response.data
      data = data.map(item => ({...item, rating: "0"}))
    })
  return data
}

export const getProductMatches = async(num_of_items, rated_products) => {
    
  var data

  try {
    await axios.post("http://localhost:8000/api/getProductMatches/" + num_of_items.toString(), rated_products, 
      {
        headers: {'Content-Type': 'application/json'}
      }
    ).then(response => {data = response.data})
  
  } catch (error) {
    console.log(error)
  }
  
  return data
}


