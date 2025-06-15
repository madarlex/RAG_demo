from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rag.rag_singleton import qa_chain

@csrf_exempt
def chat_view(request):
    chat_history = request.session.get("chat_history", [])

    if request.method == 'POST':
        query = request.POST.get("query")
        if query:
            result = qa_chain.invoke({"query": query})
            answer = result["result"]
            chat_history.append({"query": query, "answer": answer})
            request.session["chat_history"] = chat_history
        return redirect("chat_view")

    return render(request, "chat.html", {"chat_history": chat_history})

def clear_chat(request):
    request.session.pop("chat_history", None)
    return redirect("chat_view")