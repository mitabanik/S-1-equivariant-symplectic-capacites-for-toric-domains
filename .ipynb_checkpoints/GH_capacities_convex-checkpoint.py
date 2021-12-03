{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f71a2e93",
   "metadata": {},
   "outputs": [],
   "source": [
    "def HG_capacities_conv(it,x,f):\n",
    "    cap=[]\n",
    "    for n in range(1,it+1):\n",
    "        Min=1e09;m=len(x);\n",
    "        for i in range(n):\n",
    "            A=[i,n-i]; Max=np.dot(A, [0 ,1]);\n",
    "            Max=max(max(np.dot(A,[x,f])),Max)\n",
    "            \n",
    "            if Max<=Min:\n",
    "                Min=Max\n",
    "                \n",
    "        cap.append(Min)\n",
    "    return cap\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
