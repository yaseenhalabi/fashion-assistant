import { useState } from "react"
function RevealText(props){
  const [isOpen, setIsOpen] = useState(false)

  const toggleOpen = () => {
    setIsOpen(!isOpen)
  }

  return (
    <>    
      <div className="flex items-center cursor-pointer select-none" onClick={toggleOpen}>
        <span className="mr-2">How to Use</span>
        <span className={`transform transition-transform ${isOpen ? 'rotate-90' : ''}`}>
          →
        </span>
      </div>
  
      <div className={`transition-height duration-300 ${isOpen ? 'max-h-40' : 'max-h-0'} overflow-hidden`}>
        More text that was revealed!
      </div>
    </>
  )
}

export default RevealText
