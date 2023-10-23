class Solution {
    public List<List<Integer>> generate(int n) {
        List<List<Integer>> list=new ArrayList<>();
        List<Integer> p=new ArrayList<>();
        p.add(1);
        list.add(p);
        for(int i=1;i<n;i++){
            List<Integer> al=new ArrayList<>();
            List<Integer> temp=new ArrayList<>(list.get(i-1));
            for(int j=0;j<=i;j++){
                if(j==0 || j==i){
                    al.add(1);
                }
                else{
                    int sum=temp.get(j-1)+temp.get(j);
                    al.add(sum);
                }
            }
            list.add(al);
        }
        return list;
    }
}