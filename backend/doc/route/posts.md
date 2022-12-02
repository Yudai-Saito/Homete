# Posts

## GET /post

クエリストリングで３状態の JSON を返す。

- 通常投稿取得 : /post
- 新規投稿取得 : /post?created_at="2022-11-24"&update="new"
- 過去投稿取得 : /post?created_at="2022-11-24"&update="new"

```SQL
select
  post.id,
  json_arrayagg(
    json_object(
      "head", post.head,
      "face", post.face,
      "facialhair", post.facialhair,
      "accessories", post.accessories,
      "skincolor", post.skincolor,
      "clothingcolor", post.clothingcolor,
      "haircolor", post.haircolor
    )
  ) as icon,
  post.name, post.created_at, post.contents,
  json_arrayagg(
    json_object(
      "reaction", pr.post_reactions,
      "count",
      case
        when post.user_id = 1 then pr.reaction_count
        when post.private = 1 then null
        else pr.reaction_count
      end
    )
  ) as post_reactions,
  ur.user_reaction
from
  posts as post
  left join (
    select
      post_id,
      (
        select
          reaction
        from
          reactions
        where
          reactions.id = post_reactions.reaction_id
      ) as post_reactions,
      count(reaction_id) as reaction_count
    from
      post_reactions
    group by
      post_id, reaction_id
  ) as pr on post.id = pr.post_id
  left join (
    select
      post_id,
      json_arrayagg(
        (
          select
            reaction
          from
            reactions
          where
            reactions.id = post_reactions.reaction_id
        )
      ) as user_reaction
    from
      post_reactions
    where
      user_id = 1
    group by
      post_reactions.post_id
  ) as ur on pr.post_id = ur.post_id
where deleted_at is null
group by
  post.id, pr.post_id, ur.post_id, ur.user_reaction;
```
