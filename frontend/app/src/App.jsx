import Product from "./Product"
import {useState, useEffect} from "react"
import axios from "axios"
import ReactLoading from 'react-loading' 
function App() {
  
  const [productDataList, setProductDataList] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const commenceScraping = async() => {
    setIsLoading(true)
    await axios.get(`http://localhost:8000/api/getAvailableProducts`)
      .then(res => {
        setProductDataList(res.data)
        setIsLoading(false)
      }
    )
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
    const sharedClassName = "m-auto mt-56"
    const startButton = <button className={sharedClassName + " text-2xl bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg"} onClick={() => commenceScraping()}>Commence Scraping</button>
    const loading = <ReactLoading className={sharedClassName} type="spinningBubbles" color="black" height={667} width={375} />

    cardElements = isLoading? loading : startButton
  }
  return (

  <div className="flex flex-wrap">
    {cardElements}
      
     {productDataList.length !== 0? <button className="bg-blue-500 text-white hover:bg-blue-700 py-2 px-4 font-bold rounded-lg m-auto">Submit</button>: ""}

    </div>


  )
}

export default App
