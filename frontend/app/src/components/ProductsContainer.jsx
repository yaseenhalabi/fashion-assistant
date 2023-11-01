import {useState} from "react"
import ReactLoading from 'react-loading' 
import Product from "./Product"
import { getProducts, getProductMatches } from "../services/ProductService"  

function ProductsContainer() {

  const [productDataList, setProductDataList] = useState([])
  const [isLoading, setIsLoading] = useState(false)

  const setProducts = async(num_of_items) => {
    setIsLoading(true)
    const data = await getProducts(num_of_items)
    console.log(data)
    setProductDataList(data)
    setIsLoading(false)
  }

  const setProductMatches = async(num_of_items) => {
    const data = await getProductMatches(num_of_items, productDataList)
    console.log(data) 
    setProductDataList(data)         
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
      key={item.url}
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
  const startButton = <button className={"text-2xl bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg"} onClick={() => setProducts(2)}>Commence Scraping</button>
  const loadingElement = <ReactLoading className="m-auto mt-56" type="spinningBubbles" color="black" height={667} width={375} />
  const buttonThenLoading = isLoading? loadingElement : <div className="m-auto mt-56">{startButton}<p className="text-center">This may take a minute</p></div>

  
  return (

  <div className="flex flex-wrap">
    {productDataList.length == 0? buttonThenLoading: ""}
    {cardElements}
    {productDataList.length !== 0? <button onClick={() => setProductMatches(2)} className="bg-blue-500 text-white hover:bg-blue-700 py-2 px-4 font-bold rounded-lg m-auto">Submit</button>: ""}
    </div>

  )
}

export default ProductsContainer
