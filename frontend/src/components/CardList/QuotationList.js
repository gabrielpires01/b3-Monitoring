import { useEffect, useState } from "react"
import styled from "styled-components"
import { getQuotations } from "../../services/api"
import QuotationCard from "../Card/QuotationCard"

function QuotationList ({symbol, interval}) {
	const [quotations, setQuotations] = useState()
	const [listQuot, setListQuot] = useState()

	useEffect(() => {
		const promise = getQuotations(symbol,interval)
		promise.then(res => {
			const list = [];
			setQuotations(res)
			for (const [key, value] of Object.entries(res)) {
				list.push(<QuotationCard time={key} quotation={value}/>)
			}
			setListQuot(list)
		})
		.catch(err => alert(err))

		
		
	}, [])

	return (
		<Component>
			<Title>Quotations for {symbol} in the interval of {interval} each</Title>
			<List>
				{listQuot}
			</List>
		</Component>
		
	)
}

const Component = styled.div`
	display: flex;
	flex-direction: column;
	align-items: center;
	margin: 0 20px;
`

const List = styled.div`
	display: flex;
	width: 100%;
	flex-wrap: wrap;
	align-items: center;
	justify-content: space-around;
`

const Title = styled.h1`
	font-size: 30px;
	font-family: "Kaniti";
	text-align: center;
	margin: 30px;
`

export default QuotationList