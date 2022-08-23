import styled from "styled-components"
import SearchBar from "./SearchBar"

function Header () {
	return (
		<Component>
			<Title>Search Updated Quotation History</Title>
			<SearchBar />
		</Component>
	)
}

const Title = styled.h1`
	font-size: 20px;
`

const Component = styled.div`
	width: calc(100% - 30px);

	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	margin-top: 20px !important;
`

export default Header