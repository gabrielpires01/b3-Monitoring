import PipelineList from "../CardList/PipelineList"
import styled from "styled-components"
import CreatePipeline from "../CreatePipeline/CreatePipeline"
import { useState } from "react"
import Header from "../Header/Header"

function Home () {
	const [update, setUpdate] = useState(false)
	
	return (
		<Component>
			<Header />
			<CreatePipeline setUpdate={setUpdate}/>
			<PipelineList update={update}/>
		</Component>
	)
}

const Component = styled.div`
	display: flex;
	flex-direction: column;
	align-items: center;
	div {
		margin: 20px;
	}
`


export default Home