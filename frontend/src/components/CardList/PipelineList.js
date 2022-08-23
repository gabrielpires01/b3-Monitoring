import { useEffect, useState } from "react"
import { getPipelines } from "../../services/api"
import PipelineCard from "../Card/PipelineCard"
import styled from "styled-components"

function PipelineList ({update}) {
	const [pipelines, addPipelines] = useState([])

	useEffect(() => {
		const promise = getPipelines()
		promise.then(res => addPipelines(res))
			.catch(err => console.error(err))
	}, [update])

	return (
		<Component>
			<Title>Your Pipelines</Title>
			<List>
				{
					pipelines.map((pipeline, index) => <PipelineCard pipeline={pipeline} key={`pipeline-${index}`}/>)
				}
			</List>
		</Component>
		
	)
}

const Component = styled.div`
	display: flex;
	flex-direction: column;
	align-items: center;
`
const List = styled.div`
	display: flex;
	width: 100%;
	flex-wrap: wrap;
	align-items: center;
	justify-content: center;
`

const Title = styled.h1`
	font-size: 30px;
	font-family: "Kaniti";
`

export default PipelineList