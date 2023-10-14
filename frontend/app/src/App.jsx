// sorry!! my frontend code is a mess


import Product from "./Product"
import {useState, useEffect} from "react"
import axios from "axios"
import ReactLoading from 'react-loading' 
import { fas } from "@fortawesome/free-solid-svg-icons"
function App() {
   
  const [productDataList, setProductDataList] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [numItemsRequested, setNumItemsRequested] = useState(20)
  //  api calls
  const commenceScraping = async() => {
    setIsLoading(true)
    await axios.get(`http://localhost:8000/api/getAvailableProducts/` + numItemsRequested.toString())
      .then(res => {
        setProductDataList(res.data)
        setProductDataList(list => list.map(item => ({...item, rating: "0"})));

        setIsLoading(false)
      }
    )
  }
  
  const sendBackRatings = async() => {
    try {
      await axios.post("http://localhost:8000/api/findNewProducts/" + numItemsRequested.toString(), productDataList, 
      {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(res => {setProductDataList(res.data)})
        
    } catch (error) {
      console.log(error)
    }
      
  }

  // callback funciton that gets the star rating 
  const updateProductRating = (index, newRating) => {
    const updatedProducts = [...productDataList];
    updatedProducts[index].rating = newRating.toString();
    setProductDataList(updatedProducts);
  };

  // map objects in productDataList 
  let cardElements = productDataList.map((item,index) =>  
    <Product
      onRatingChange={(newRating) => updateProductRating(index, newRating)}
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

  //what user sees first
  const startButton = <button className={"text-2xl bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg"} onClick={() => commenceScraping()}>Commence Scraping</button>
  const loadingElement = <ReactLoading className="m-auto mt-56" type="spinningBubbles" color="black" height={667} width={375} />
  const buttonThenLoading = isLoading? loadingElement : <div className="m-auto mt-56">{startButton}<p className="text-center">This may take a minute</p></div>

  
  return (

  <div className="flex flex-wrap">
    {productDataList.length == 0? buttonThenLoading: ""}

    {cardElements}

    {productDataList.length !== 0? <button onClick={() => sendBackRatings()} className="bg-blue-500 text-white hover:bg-blue-700 py-2 px-4 font-bold rounded-lg m-auto">Submit</button>: ""}

    </div>


  )
}

export default App
