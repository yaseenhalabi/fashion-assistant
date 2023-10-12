import { useState } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCoffee } from '@fortawesome/free-solid-svg-icons';

function Product(props){


  const [rating, setRating] = useState(0) 
 
  const starRating = []

  for (let i = 0; i<5; i++)
    {
      starRating.push(
        <button className="text-lg select-none" onClick={() => setRating(i)}>
          {i<=rating? <div>★</div> : <div>☆</div>}
        </button>
      )
    } 
  
  return (

    <>
      
    <div className="max-h-auto lg:basis-6/12 sm:basis-full mx-auto">


      <div className="md:flex">
        <div className="md:flex-shrink-0">
          <img className="h-full w-full object-cover md:w-48" src={props.imageAddress} alt="IMAGE MISSING" />
          </div>
          <div className="p-8 pt-0">
            <div className="flex">{starRating}</div>
            <div className="uppercase tracking-wide text-sm text-indigo-500 font-semibold">
              <a href={props.url} className="hover:underline">{props.tags}</a>
            </div>
            <p className="block mt-1 text-lg leading-tight font-medium text-black hover:underline">
              Price: <span className="font-bold">{props.price}</span>
            </p>
            <p className="mt-2 text-gray-500">Size: <strong>{props.size}</strong></p>
            <p className="text-gray-500">Color: <strong>{props.color}</strong></p>
            <p className="text-gray-500">Condition: <strong>{props.condition}</strong></p>
            <div className="h-20 overflow-y-auto text-gray-500 max-w-sm border-t mt-2 pt-2"> 
                Description: {props.description}
            </div>

          </div>

        </div>
    </div>

    </>
  )
}


export default Product
