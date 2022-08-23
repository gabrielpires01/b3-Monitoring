import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import styled from "styled-components";
import { getQuotations } from "../../services/api";
import QuotationList from "../CardList/QuotationList";

function Quotation () {
	const navigate = useNavigate();
	const {state} = useLocation();

	useEffect(() => {
		if(!state) {
			alert("Search a symbol with especific interval")
			navigate("/")
		}
	}, [])

	return (
		<Component>
			<QuotationList symbol={state?.symbol} interval={state?.interval} />
		</Component>
	)
}

const Component = styled.div`

`

export default Quotation