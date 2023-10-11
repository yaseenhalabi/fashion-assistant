import Product from "./Product"
import {useState, useEffect} from "react"
import axios from "axios"
function App() {
  
  const [productDataList, setProductDataList] = useState([])

  const commenceScraping = async() => {
    await axios.get(`http://localhost:8000/api/getAvailableProducts`)
      .then(res => setProductDataList(res.data))
  }

  let cardElements
  if (productDataList.length !== 0){
    cardElements = productDataList.map(item => 
      <Product 
        color={item.color}
        condition={item.condition}
        description={item.description}
        imageAddress={item.image}
        price={item.price}
        size={item.size}
        tags={item.tags}
        url={item.url}

      />
    )
  }

  else{
    cardElements = <button onClick={() => commenceScraping()}>Commence Scraping</button>
  }
  return (

  <div className="flex flex-wrap">
    {cardElements}
  </div>


  )
}

export default App
