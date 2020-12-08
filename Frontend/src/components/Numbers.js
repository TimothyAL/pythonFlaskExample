import React, {useState} from "react";

const axios = require('axios').default;

function Numbers(props) {
    const [state, setState] = useState({
        number1: 0,
        number2: 0
    });

    const handleAnswer = (number) => {
        setState({
            ...state,
            answer: number
        })
    }

    const handleAdd = async() => {
        const responce = await axios.get(`back/functions/add/${state.number1}&${state.number2}`)
        handleAnswer(responce.data)
        }

    const handleSubtract = async() => {
        const response = await axios.get(`back/functions/subtract/${state.number1}&${state.number2}`)
        handleAnswer(response.data)
    }

    const handleMultiply = async() => {
        const response = await axios.get(`back/functions/multiply/${state.number1}&${state.number2}`)
        handleAnswer(response.data)
    }

    const handleDivide = async() => {
        const response = await axios.get(`back/functions/divide/${state.number1}&${state.number2}`)
        handleAnswer(response.data)
    }

    const handleExponentiation = async() => {
        const response = await axios.get(`back/functions/exponent/${state.number1}&${state.number2}`)
        handleAnswer(response.data)
    }


    const handleNumberChange = (event) => {
        setState({
            ...state,
            [event.target.name]: event.target.value
        });
    }



    return(
        <>
            <label>First Number</label>
            <input type='text' name='number1' onChange={handleNumberChange}/>
            <label>Second Number</label>
            <input type='text' name='number2' onChange={handleNumberChange}/>
            <br/>
            <button onClick={handleAdd}>Add(+)</button>
            <button onClick={handleSubtract}>Subtract(-)</button>
            <button onClick={handleMultiply}>Multiply(*)</button>
            <button onClick={handleDivide}>Divide(/)</button>
            <button onClick={handleExponentiation}>Exponentiate(+)</button>

            <label>{state.answer? <>Answer: {state.answer}</>:<></>}</label>
        </>
    )
}

export default Numbers;