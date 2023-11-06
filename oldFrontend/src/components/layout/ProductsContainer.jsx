import {useState, useEffect} from "react"
import Product from "../common/Product"
import LoadingAnimation from "../common/LoadingAnimation"
import { getProducts, getProductMatches } from "../../services/ProductService"  


function ProductsContainer() {

  const [productDataList, setProductDataList] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  
  const fetchProducts = async(num_of_items) => {

    try {
      setIsLoading(true)
      const data = await getProducts(num_of_items)
      console.log(data)
      setProductDataList(data)
    }

    catch(error) {
      console.error(error)
    }

    finally {
      setIsLoading(false)
    }
  }

  const fetchProductMatches = async(num_of_items) => {
    try{
      const data = await getProductMatches(num_of_items, productDataList)
      setProductDataList(data)         
    }
    catch(error){
      console.error(error)
    }
  }
  
  useEffect(() => {
    fetchProducts(2)
  }, [])
  // callback funciton that gets the star rating 
  const updateProductRating = (index, newRating) => {
    const updatedProducts = [...productDataList];
    updatedProducts[index].rating = newRating.toString();
    setProductDataList(updatedProducts); };

  // map objects in productDataList 
  let renderProductCards
  if (productDataList.length != 0){
    renderProductCards = productDataList.map((item,index) =>  
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

  } 
  //what user sees first

  const renderLoading = isLoading? <LoadingAnimation/> : ""
  
    // <StartButton function={() => fetchProducts(2)}/>

  const renderFindMatchesButton = () => {
    return (
      <button 
        onClick={() => fetchProductMatches(2)} 
        className="bg-blue-500 text-white hover:bg-blue-700 py-2 w-full font-bold my-8">
        Find Matches
      </button>
    )
  }
  return (

    <div className="flex flex-wrap">
      {productDataList.length == 0 && renderLoading}
      {renderProductCards}
      {productDataList.length !== 0 && renderFindMatchesButton()}
    </div>

  )
}

export default ProductsContainer
