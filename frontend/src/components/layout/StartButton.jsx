function StartButton(props){

  return(
    <div className="m-auto mt-56">
      <button 
        className="text-2xl bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg" 
        onClick={props.function}>
        Commence Scraping
      </button>
      <p className="text-center">This may take a minute</p>
    </div>
  )

}

export default StartButton
