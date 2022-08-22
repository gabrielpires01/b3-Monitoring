import PipelineList from "../CardList/PipelineList"
import styled from "styled-components"
import CreatePipeline from "../CreatePipeline/CreatePipeline"
import { useState } from "react"

function Home () {
	const [update, setUpdate] = useState(false)
	
	return (
		<Component>
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