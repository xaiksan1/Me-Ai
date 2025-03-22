import { Box, Container, VStack, Heading, Text, Input, Button, useToast } from "@chakra-ui/react"
import { useState } from "react"

export default function Home() {
  const [input, setInput] = useState("")
  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)
  const toast = useToast()

  const handleSubmit = async () => {
    if (!input.trim()) return

    setLoading(true)
    try {
      const response = await fetch("/api/v1/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: input })
      })

      const data = await response.json()
      setMessages(prev => [...prev, 
        { role: "user", content: input },
        { role: "assistant", content: data.response }
      ])
      setInput("")
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to get response",
        status: "error",
        duration: 3000,
        isClosable: true,
      })
    }
    setLoading(false)
  }

  return (
    <Container maxW="container.md" py={10}>
      <VStack spacing={8}>
        <Heading>Me-AI Assistant</Heading>
        <Text>Your Tech-Savvy AI Companion</Text>
        
        <Box w="100%" h="60vh" overflowY="auto" bg="gray.50" p={4} borderRadius="md">
          {messages.map((msg, i) => (
            <Box 
              key={i}
              bg={msg.role === "user" ? "blue.50" : "green.50"}
              p={3}
              my={2}
              borderRadius="md"
            >
              <Text>{msg.content}</Text>
            </Box>
          ))}
        </Box>

        <Box w="100%" display="flex" gap={2}>
          <Input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask me anything..."
            onKeyPress={(e) => e.key === "Enter" && handleSubmit()}
          />
          <Button 
            colorScheme="blue" 
            onClick={handleSubmit}
            isLoading={loading}
          >
            Send
          </Button>
        </Box>
      </VStack>
    </Container>
  )
}
